/* global api */
class en_Cambridge {
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
        // Chỉ cần gọi hàm findCambridge
        return this.findCambridge(word);
    }

    async findCambridge(word) {
        let notes = [];
        if (!word) return notes;

        // Helper function to get text content from a node
        function T(node) {
            return node ? node.innerText.trim() : '';
        }

        // URL for English-English dictionary
        let base = 'https://dictionary.cambridge.org/dictionary/english/';
        let url = base + encodeURIComponent(word);
        let doc;
        try {
            let data = await api.fetch(url);
            let parser = new DOMParser();
            doc = parser.parseFromString(data, 'text/html');
        } catch (err) {
            return [];
        }

        let entries = doc.querySelectorAll('.pr.entry-body__el') || [];
        for (const entry of entries) {
            let definitions = [];
            let audios = [];

            let expression = T(entry.querySelector('.di-title .hw'));
            if (!expression) continue;

            let reading = '';
            let reading_uk_el = entry.querySelector('.uk .ipa');
            let reading_us_el = entry.querySelector('.us .ipa');
            if (reading_uk_el) reading += `UK <span class="ipa">/${T(reading_uk_el)}/</span> `;
            if (reading_us_el) reading += `US <span class="ipa">/${T(reading_us_el)}/</span>`;
            
            let pos = T(entry.querySelector('.posgram.dpos-g .pos'));
            pos = pos ? `<span class='pos'>${pos}</span>` : '';

            let audio_uk_el = entry.querySelector('.uk source[type="audio/mpeg"]');
            if (audio_uk_el) audios.push('https://dictionary.cambridge.org' + audio_uk_el.getAttribute('src'));
            
            let audio_us_el = entry.querySelector('.us source[type="audio/mpeg"]');
            if (audio_us_el) audios.push('https://dictionary.cambridge.org' + audio_us_el.getAttribute('src'));

            let sense_blocks = entry.querySelectorAll('.pr.dsense') || [];
            for (const block of sense_blocks) {
                let def_blocks = block.querySelectorAll('.def-block.ddef_block') || [];
                for (const def_block of def_blocks) {
                    let eng_tran = T(def_block.querySelector('.def.ddef_d'));
                    if (!eng_tran) continue;
                    
                    let definition = '';
                    
                    // Add part of speech if it's not a sub-definition
                    if (!block.closest('.phrase-block')) {
                        definition += pos;
                    }
                    
                    definition += `<span class='eng_tran'>${eng_tran}</span>`;

                    let examples = def_block.querySelectorAll('.examp.dexamp') || [];
                    if (examples.length > 0 && this.maxexample > 0) {
                        definition += '<ul class="sents">';
                        for (const [index, examp] of examples.entries()) {
                            if (index >= this.maxexample) break;
                            let eng_examp = T(examp.querySelector('.eg'));
                            if (eng_examp) {
                                // Bold the searched word in the example
                                const regex = new RegExp(`\\b(${this.word})\\b`, 'gi');
                                eng_examp = eng_examp.replace(regex, `<b>$1</b>`);
                                definition += `<li class='sent'><span class='eng_sent'>${eng_examp}</span></li>`;
                            }
                        }
                        definition += '</ul>';
                    }
                    definitions.push(definition);
                }
            }
            
            if (definitions.length > 0) {
                let css = this.renderCSS();
                notes.push({
                    css,
                    expression,
                    reading,
                    definitions,
                    audios
                });
            }
        }
        return notes;
    }

    renderCSS() {
        return `
            <style>
                span.ipa { color: #888; }
                span.pos { text-transform: lowercase; font-size: 0.9em; margin-right: 5px; padding: 2px 4px; color: white; background-color: #0d47a1; border-radius: 3px; }
                span.eng_tran { margin: 0; padding: 0; }
                ul.sents { font-size: 0.9em; list-style: square inside; margin: 5px 0; padding: 5px; background: rgba(13, 71, 161, 0.1); border-radius: 5px; }
                li.sent { margin: 0; padding: 2px 0; }
                span.eng_sent { margin-right: 5px; }
            </style>`;
    }
}
