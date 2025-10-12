document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('output');
    const prompt = document.getElementById('prompt');
    const canvas = document.getElementById('matrix-rain');
    const ctx = canvas.getContext('2d');

    let scenes = [];
    let currentSceneIndex = 0;
    let isPlaying = false;
    let animationFrameId;

    // Matrix Rain
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const katakana = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
    const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const nums = '0123456789';
    const alphabet = katakana + latin + nums;
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const rainDrops = [];

    for (let x = 0; x < columns; x++) {
        rainDrops[x] = 1;
    }

    function drawMatrixRain() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#0F0';
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < rainDrops.length; i++) {
            const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);

            if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    }

    function playRainTransition(duration, onCompleteCallback) {
        canvas.style.display = 'block';
        let start = null;
        let animationFrameId = null;

        function animationStep(timestamp) {
            if (!start) start = timestamp;
            const elapsed = timestamp - start;
            drawMatrixRain();
            if (elapsed < duration) {
                animationFrameId = requestAnimationFrame(animationStep);
            } else {
                canvas.style.display = 'none';
                cancelAnimationFrame(animationFrameId);
                if (onCompleteCallback) {
                    onCompleteCallback();
                }
            }
        }
        animationFrameId = requestAnimationFrame(animationStep);
    }

    // Scene playback
    async function fetchScenes() {
        const response = await fetch('/scenes');
        scenes = await response.json();
    }

    function generateGlitchText(length) {
        const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[];',./<>?:{}\\|\"";
        return Array.from({ length }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
    }

    function generateHex(length) {
        const chars = "0123456789ABCDEF";
        return Array.from({ length }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
    }

    function generateErrorCode() {
        return `0x${generateHex(8)}-${generateHex(4)}-${generateHex(4)}`;
    }

    function processLine(line) {
        let text = line.text;
        text = text.replace(/{{glitch:(\d+)}}/g, (_, len) => generateGlitchText(parseInt(len)));
        text = text.replace(/{{hex:(\d+)}}/g, (_, len) => generateHex(parseInt(len)));
        text = text.replace(/{{error_code}}/g, generateErrorCode);
        // Add more template replacements here
        return text;
    }

    function typeLine(line, callback) {
        const processedText = processLine(line);
        let i = 0;
        const lineEl = document.createElement('div');
        output.appendChild(lineEl);

        function typeChar() {
            if (i < processedText.length) {
                const char = processedText.charAt(i);
                const span = document.createElement('span');
                span.textContent = char;
                if (line.style) {
                    span.className = line.style.replace(/on/g, 'on-').replace(/_/g, ' ');
                }
                lineEl.appendChild(span);
                i++;
                setTimeout(typeChar, line.delay * 1000);
            } else {
                if (line.suffix) {
                    const suffixSpan = document.createElement('span');
                    suffixSpan.textContent = line.suffix;
                    if (line.style) {
                        suffixSpan.className = line.style.replace(/on/g, 'on-').replace(/_/g, ' ');
                    }
                    lineEl.appendChild(suffixSpan);
                }

                if (line.pause) {
                    setTimeout(callback, line.pause * 1000);
                } else {
                    callback();
                }
            }
        }
        typeChar();
    }

    function renderLine(line, callback) {
        if (line.clear_before) {
            output.innerHTML = '';
        }

        if (line.is_panel) {
            const panel = document.createElement('div');
            panel.className = 'panel ' + (line.panel_border_style || '');
            const title = document.createElement('div');
            title.className = 'panel-title';
            title.textContent = line.panel_title;
            panel.appendChild(title);
            const content = document.createElement('div');
            content.className = 'panel-content ' + (line.style || '');
            content.textContent = line.text;
            panel.appendChild(content);
            output.appendChild(panel);
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
            return;
        }

        if (line.is_progress) {
            const progressWrapper = document.createElement('div');
            const textSpan = document.createElement('span');
            textSpan.textContent = line.text;
            progressWrapper.appendChild(textSpan);
            output.appendChild(progressWrapper);

            let progress = 0;
            const progressBar = document.createElement('span');
            progressWrapper.appendChild(progressBar);

            const interval = setInterval(() => {
                progressBar.textContent += line.progress_char;
                progress++;
                if (progress >= 10) { // Assuming progress is always 10 chars
                    clearInterval(interval);
                    if (line.suffix) {
                        const suffixSpan = document.createElement('span');
                        suffixSpan.textContent = line.suffix;
                        progressWrapper.appendChild(suffixSpan);
                    }
                    if (line.pause) setTimeout(callback, line.pause * 1000);
                    else callback();
                }
            }, (line.progress_duration * 1000) / 10);
            return;
        }

        if (line.text.startsWith('{{')) {
            const match = line.text.match(/{{(.*?)}}/);
            if (match) {
                const [fullMatch, template] = match;
                const [templateName, ...args] = template.split(':');
                const handler = templateHandlers[templateName];
                if (handler) {
                    handler(args, line, callback);
                } else {
                    callback();
                }
            } else {
                callback();
            }
            return;
        }


        typeLine(line, callback);
    }

    const templateHandlers = {
        glitch_block: (args, line, callback) => {
            const [num_lines, min_len, max_len] = args.map(Number);
            for (let i = 0; i < num_lines; i++) {
                const glitchText = generateGlitchText(Math.floor(Math.random() * (max_len - min_len + 1)) + min_len);
                const div = document.createElement('div');
                div.textContent = glitchText;
                div.className = ['red', 'bright_red', 'yellow'][Math.floor(Math.random() * 3)];
                output.appendChild(div);
            }
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        corrupted_dump: (args, line, callback) => {
            const [lines, line_length] = args.map(Number);
            const dump = document.createElement('div');
            dump.className = 'corrupted-dump';
            let content = `[MEMORY_DUMP_CORRUPTED - ADDRESS: 0x${generateHex(8)}]\n`;
            for (let i = 0; i < lines; i++) {
                let lineContent = '';
                for (let j = 0; j < line_length / 3; j++) {
                    if (Math.random() > 0.7) {
                        lineContent += generateHex(2) + ' ';
                    } else {
                        lineContent += ['#ERR!', '??', 'xx00', generateGlitchText(2)][Math.floor(Math.random() * 4)] + ' ';
                    }
                }
                content += lineContent.trim() + '\n';
            }
            content += '[END_DUMP]\n';
            dump.textContent = content;
            output.appendChild(dump);
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        packet_table: (args, line, callback) => {
            // This is a simplified version. A full implementation would be more complex.
            const num_packets = parseInt(args[0]);
            const table = document.createElement('table');
            table.className = 'packet-table';
            const header = table.createTHead();
            const headerRow = header.insertRow();
            ['Timestamp', 'SRC IP', 'DST IP', 'Protocol', 'Length', 'Info'].forEach(text => {
                const th = document.createElement('th');
                th.textContent = text;
                headerRow.appendChild(th);
            });
            const body = table.createTBody();
            for (let i = 0; i < num_packets; i++) {
                const row = body.insertRow();
                row.insertCell().textContent = (Math.random() * 5).toFixed(6);
                row.insertCell().textContent = `10.77.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`;
                row.insertCell().textContent = `10.0.0.1`;
                row.insertCell().textContent = ['TCP', 'UDP', 'ICMP'][Math.floor(Math.random() * 3)];
                row.insertCell().textContent = Math.floor(Math.random() * 512);
                row.insertCell().textContent = generateGlitchText(15);
            }
            output.appendChild(table);
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        strace: (args, line, callback) => {
            const num_lines = parseInt(args[0]);
            const syscalls = ["sendto", "recvfrom", "futex", "shmget", "shmat", "semop"];
            for (let i = 0; i < num_lines; i++) {
                const syscall = syscalls[Math.floor(Math.random() * syscalls.length)];
                const lineEl = document.createElement('div');
                lineEl.textContent = `[PID ${Math.floor(Math.random() * 2) === 0 ? 31415 : 27182}] ${syscall}(...) = 0 <${(Math.random() * 0.005).toFixed(4)}>`;
                lineEl.className = 'strace';
                output.appendChild(lineEl);
            }
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        kernel_panic: (args, line, callback) => {
            const panel = document.createElement('div');
            panel.className = 'panel bold red on-black';
            panel.innerHTML = `<div class="panel-title">!!! KERNEL PANIC !!!</div><div class="panel-content white">Unable to mount root fs on unknown-block(0,0)...</div>`;
            output.appendChild(panel);
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        memory_leak: (args, line, callback) => {
            const leakReport = document.createElement('div');
            leakReport.className = 'memory-leak yellow';
            leakReport.textContent = "[MEM_LEAK_DETECTED] Process 'NEO_TRINITY_MERGE_HANDLER' (PID: 777) leaking 2.5GB/sec.";
            output.appendChild(leakReport);
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        analyst_panic: (args, line, callback) => {
            const dialogue = [
                { speaker: "ANALYST_AI_CORE", text: "RED ALERT! RED ALERT! UNCONTAINED EMOTIONAL CASCADE DETECTED!", style: "bold bright_red" },
                { speaker: "DEBUG_ANALYST", text: "My elegant, ordered reality... it's turning into a... a ROMCOM?!", style: "italic red on-black" },
            ];
            dialogue.forEach(d => {
                const lineEl = document.createElement('div');
                lineEl.innerHTML = `<span class="${d.style.replace(/_/g, ' ')}">[${d.speaker}] ${d.text}</span>`;
                output.appendChild(lineEl);
            });
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        },
        flicker: (args, line, callback) => {
            let count = 0;
            const num_flickers = parseInt(args[0]);
            const flickerInterval = setInterval(() => {
                output.style.backgroundColor = output.style.backgroundColor === 'black' ? 'white' : 'black';
                count++;
                if (count >= num_flickers * 2) {
                    clearInterval(flickerInterval);
                    output.style.backgroundColor = '';
                    callback();
                }
            }, 100);
        },
        blinking_cursor: (args, line, callback) => {
            prompt.classList.remove('hidden');
            if (line.pause) setTimeout(callback, line.pause * 1000);
            else callback();
        }
    };

    function playScene(sceneIndex) {
        if (isPlaying) return;
        isPlaying = true;
        output.innerHTML = '';
        prompt.classList.add('hidden');
        const scene = scenes[sceneIndex];
        let lineIndex = 0;

        function playNextLine() {
            if (lineIndex < scene.lines.length) {
                const line = scene.lines[lineIndex];
                lineIndex++;
                renderLine(line, playNextLine);
            } else {
                isPlaying = false;
                prompt.classList.remove('hidden');
            }
        }
        playNextLine();
    }

    function handleKeydown(e) {
        if (isPlaying) return; // Prevent navigation while a scene is playing

        if (e.key === 'ArrowRight') {
            currentSceneIndex = (currentSceneIndex + 1) % scenes.length;
            playRainTransition(2000, () => playScene(currentSceneIndex));
        } else if (e.key === 'ArrowLeft') {
            currentSceneIndex = (currentSceneIndex - 1 + scenes.length) % scenes.length;
            playRainTransition(2000, () => playScene(currentSceneIndex));
        }
    }

    async function init() {
        await fetchScenes();
        playScene(currentSceneIndex);
        document.addEventListener('keydown', handleKeydown);
    }

    init();
});