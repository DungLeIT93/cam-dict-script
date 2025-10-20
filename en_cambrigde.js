/* global api */
class encn_Cambridge {
    constructor(options) {
        this.options = options;
        this.maxexample = 2;
        this.word = '';
    }

    async displayName() {
        return 'Cambridge EN->EN Dictionary';
    }

    setOptions(options) {
        this.options = options;
        this.maxexample = options.maxexample;
    }

    async findTerm(word) {
        this.word = word;
        // Lấy dạng nguyên thể của từ (ví dụ: 'running' -> 'run')
        let deinflected = await api.deinflect(word) || [];
        let terms = (deinflected.length > 0 && deinflected[0] !== word) ? [word, deinflected[0]] : [word];
        
        let promises = terms.map(term => this.findCambridge(term));
        let results = await Promise.all(promises);
        
        // Gộp kết quả và loại bỏ các mục trống hoặc trùng lặp
        const uniqueResults = [];
        const seenExpressions = new Set();
        for (const result of results.flat()) {
            if (result && !seenExpressions.has(result.expression)) {
                uniqueResults.push(result);
                seenExpressions.add(result.expression);
            }
        }
        return uniqueResults;
    }

    async findCambridge(word) {
        if (!word) return [];
        let notes = [];
        const maxexample = this.maxexample;
        const url = `https://dictionary.cambridge.org/dictionary/english/${encodeURIComponent(word)}`;

        try {
            let doc = await api.fetch(url).then(text => new DOMParser().parseFromString(text, 'text/html'));
            
            // Tìm các khối định nghĩa chính trên trang
            let entries = doc.querySelectorAll('.pr.entry-body__el');
            if (!entries || entries.length === 0) return [];

            for (const entry of entries) {
                let expression = entry.querySelector('.di-title .hw')?.textContent.trim();
                if (!expression) continue;

                // Lấy phiên âm UK và US
                let reading_uk_el = entry.querySelector('.uk .ipa');
                let reading_us_el = entry.querySelector('.us .ipa');
                let reading = '';
                if (reading_uk_el) reading += `UK <span class="ipa">/${reading_uk_el.textContent.trim()}/</span> `;
                if (reading_us_el) reading += `US <span class="ipa">/${reading_us_el.textContent.trim()}/</span>`;

                // Lấy file âm thanh UK và US
                let audios = [];
                let audio_uk_el = entry.querySelector('.uk .audio_play_button');
                if (audio_uk_el) audios.push('https://dictionary.cambridge.org' + audio_uk_el.getAttribute('data-src-mp3'));
                let audio_us_el = entry.querySelector('.us .audio_play_button');
                if (audio_us_el) audios.push('https://dictionary.cambridge.org' + audio_us_el.getAttribute('data-src-mp3'));
                
                // Xử lý các khối định nghĩa chi tiết
                let definitions = [];
                let sense_blocks = entry.querySelectorAll('.pr.dsense');

                for (const block of sense_blocks) {
                    let definitionHTML = '';
                    
                    // Lấy loại từ (Part of Speech)
                    let pos = block.querySelector('.posgram.dpos-g .pos')?.textContent.trim() || entry.querySelector('.posgram.dpos-g .pos')?.textContent.trim();
                    if (pos) definitionHTML += `<span class='pos'>${pos}</span>`;

                    // Lấy Guideword (từ hướng dẫn)
                    let guideword = block.querySelector('.guideword.dguideword span')?.textContent.trim();
                    if (guideword) definitionHTML += `<span class='guideword'>(${guideword})</span>`;

                    // Lấy định nghĩa chính
                    let def_text = block.querySelector('.def.ddef_d')?.textContent.trim();
                    if (def_text) {
                         definitionHTML += `<div class='definition'>${def_text}</div>`;
                    } else {
                        continue; // Bỏ qua nếu không có định nghĩa
                    }

                    // Lấy các câu ví dụ
                    let examples = block.querySelectorAll('.examp.dexamp');
                    if (examples.length > 0) {
                        let sentences = '';
                        let count = 0;
                        for (const ex of examples) {
                            if (count >= maxexample) break;
                            let sent_text = ex.textContent.trim();
                            // In đậm từ đang tra cứu trong câu ví dụ
                            const regex = new RegExp(`\\b(${word})\\b`, 'gi');
                            sent_text = sent_text.replace(regex, `<b>$1</b>`);
                            sentences += `<li class='sent'><span class='eng_sent'>${sent_text}</span></li>`;
                            count++;
                        }
                        if
