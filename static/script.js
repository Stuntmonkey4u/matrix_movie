document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('output');
    const prompt = document.getElementById('prompt');
    const canvas = document.getElementById('matrix-rain');
    const ctx = canvas.getContext('2d');
    const introOverlay = document.getElementById('intro-overlay');
    const startButton = document.getElementById('start-button');
    const terminal = document.getElementById('terminal');
    const controls = document.getElementById('controls');

    let scenes = [];
    let currentSceneIndex = 0;
    let isPlaying = false;
    let playbackId = 0; // Increment this to cancel previous async loops

    // --- Matrix Rain ---
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const alphabet = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const fontSize = 16;
    let rainDrops = [];

    function initRain() {
        const columns = canvas.width / fontSize;
        rainDrops = Array(Math.floor(columns)).fill(1);
    }
    initRain();

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

    let rainAnimationId;
    function startRain() {
        canvas.style.display = 'block';
        function animate() {
            drawMatrixRain();
            rainAnimationId = requestAnimationFrame(animate);
        }
        animate();
    }

    function stopRain() {
        cancelAnimationFrame(rainAnimationId);
        canvas.style.display = 'none';
    }

    function playWipe(duration, callback) {
        startRain();
        setTimeout(() => {
            stopRain();
            if (callback) callback();
        }, duration);
    }

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        initRain();
    });

    // --- Core Logic ---
    async function fetchScenes() {
        try {
            const response = await fetch('/scenes');
            scenes = await response.json();
        } catch (e) {
            output.innerHTML = '<div class="red">CRITICAL ERROR: Failed to load reality data.</div>';
        }
    }

    function processTemplate(text) {
        return text.replace(/{{glitch:(\d+)}}/g, (_, len) => {
            const chars = "!@#$%^&*()_+[];',./<>?:{}\\|\"";
            return Array.from({ length: parseInt(len) }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
        }).replace(/{{hex:(\d+)}}/g, (_, len) => {
            return Array.from({ length: parseInt(len) }, () => "0123456789ABCDEF"[Math.floor(Math.random() * 16)]).join('');
        }).replace(/{{error_code}}/g, () => `0x${Array.from({length:8}, () => "0123456789ABCDEF"[Math.floor(Math.random()*16)]).join('')}`);
    }

    async function typeLine(line, myPlaybackId) {
        const processedText = processTemplate(line.text || "");
        const lineEl = document.createElement('div');
        if (line.style) lineEl.className = line.style.replace(/_/g, ' ');
        if (line.no_newline) lineEl.style.display = 'inline';
        output.appendChild(lineEl);

        for (let char of processedText) {
            if (myPlaybackId !== playbackId) return; // Interrupted
            const span = document.createElement('span');
            span.textContent = char;
            lineEl.appendChild(span);
            await new Promise(r => setTimeout(r, (line.delay || 0.03) * 1000));
            terminal.scrollTop = terminal.scrollHeight;
        }

        if (line.suffix) {
            const suffix = document.createElement('span');
            suffix.textContent = line.suffix;
            lineEl.appendChild(suffix);
        }
        
        terminal.scrollTop = terminal.scrollHeight;
        if (line.pause && myPlaybackId === playbackId) {
             await new Promise(r => setTimeout(r, line.pause * 1000));
        }
    }

    async function handleSpecial(line, myPlaybackId) {
        if (line.clear_before) output.innerHTML = '';
        if (myPlaybackId !== playbackId) return;

        if (line.is_panel) {
            const panel = document.createElement('div');
            panel.className = 'panel ' + (line.panel_border_style || '');
            panel.innerHTML = `<div class="panel-title">${line.panel_title}</div><div class="panel-content">${line.text}</div>`;
            output.appendChild(panel);
            if (line.pause) await new Promise(r => setTimeout(r, line.pause * 1000));
        } else if (line.is_progress) {
            const progressWrapper = document.createElement('div');
            progressWrapper.innerHTML = `<span>${line.text}</span> <span class="progress-bar"></span>`;
            output.appendChild(progressWrapper);
            const bar = progressWrapper.querySelector('.progress-bar');
            for (let i = 0; i < 20; i++) {
                if (myPlaybackId !== playbackId) return;
                bar.textContent += line.progress_char || '█';
                await new Promise(r => setTimeout(r, (line.progress_duration || 1) * 50));
            }
            if (line.suffix) progressWrapper.innerHTML += ` <span>${line.suffix}</span>`;
            if (line.pause) await new Promise(r => setTimeout(r, line.pause * 1000));
        } else if (line.text && line.text.startsWith('{{')) {
            const templateMatch = line.text.match(/{{(.*?)}}/);
            if (templateMatch) {
                const [name, arg] = templateMatch[1].split(':');
                if (name === 'flicker') {
                    for (let i = 0; i < (parseInt(arg) || 3) * 2; i++) {
                        if (myPlaybackId !== playbackId) return;
                        terminal.style.backgroundColor = terminal.style.backgroundColor === 'white' ? 'black' : 'white';
                        await new Promise(r => setTimeout(r, 100));
                    }
                    terminal.style.backgroundColor = 'black';
                } else if (name === 'glitch_block') {
                    const numLines = parseInt(arg) || 5;
                    for (let i = 0; i < numLines; i++) {
                        if (myPlaybackId !== playbackId) return;
                        const div = document.createElement('div');
                        div.textContent = Array.from({ length: 50 }, () => "!@#$%^&*()_+[];',./<>?:{}\\|\""[Math.floor(Math.random() * 28)]).join('');
                        div.className = 'red';
                        output.appendChild(div);
                        await new Promise(r => setTimeout(r, 50));
                    }
                }
            }
        } else {
            await typeLine(line, myPlaybackId);
        }
        terminal.scrollTop = terminal.scrollHeight;
    }

    async function playScene(index) {
        playbackId++;
        const myPlaybackId = playbackId;
        isPlaying = true;
        currentSceneIndex = index;
        const scene = scenes[index];

        output.innerHTML = '';
        prompt.classList.add('hidden');
        
        // Scene Header / Synopsis
        await typeLine({ text: `>>> SCENE_${index + 1}: ${scene.name.toUpperCase()}`, style: "bold green", delay: 0.02 }, myPlaybackId);
        await typeLine({ text: `>>> SYNOPSIS: ${scene.description}`, style: "dim green", delay: 0.01, pause: 0.5 }, myPlaybackId);
        await typeLine({ text: "---", style: "dim green" }, myPlaybackId);

        for (let line of scene.lines) {
            if (myPlaybackId !== playbackId) return;
            await handleSpecial(line, myPlaybackId);
        }
        
        isPlaying = false;
        if (myPlaybackId === playbackId) {
            prompt.classList.remove('hidden');
        }
    }

    async function runBootSequence(e) {
        if (e && e.target) e.target.blur();
        playbackId++;
        const myPlaybackId = playbackId;
        isPlaying = true;
        
        introOverlay.classList.add('hidden');
        terminal.classList.remove('hidden');
        controls.classList.remove('hidden');
        output.innerHTML = '';
        prompt.classList.add('hidden');

        const bootLines = [
            { text: "MARS BIOS v4.0.1", delay: 0.01 },
            { text: "Check RAM: 1048576KB OK", delay: 0.01 },
            { text: "Initializing Reality Interface...", delay: 0.02 },
            { text: "Detecting anomalous signatures...", delay: 0.02 },
            { text: "Connecting to Zion Mainframe...", delay: 0.05, suffix: " FAILED." },
            { text: "Retrying via Proxy Node 7...", delay: 0.02, suffix: " SUCCESS." },
            { text: "Login: operator", delay: 0.05 },
            { text: "Password: ****************", delay: 0.02 },
            { text: "Welcome, Operator. System Diagnostic starting...", delay: 0.02, pause: 0.5 }
        ];

        for (let line of bootLines) {
            if (myPlaybackId !== playbackId) return;
            await typeLine(line, myPlaybackId);
        }

        isPlaying = false;
        if (myPlaybackId === playbackId) {
            currentSceneIndex = 0;
            playWipe(1000, () => playScene(0));
        }
    }

    // --- Navigation ---
    function handleNavigation(e) {
        if (introOverlay.offsetParent === null) { // Only if not on intro screen
            if (e.key === 'ArrowRight') {
                if (currentSceneIndex < scenes.length - 1) {
                    if (isPlaying) {
                        currentSceneIndex++;
                        playWipe(500, () => playScene(currentSceneIndex));
                    } else {
                        currentSceneIndex++;
                        playWipe(500, () => playScene(currentSceneIndex));
                    }
                } else if (!isPlaying) {
                    window.location.href = '/thanks';
                }
            } else if (e.key === 'ArrowLeft') {
                currentSceneIndex = Math.max(0, currentSceneIndex - 1);
                playWipe(500, () => playScene(currentSceneIndex));
            }
        }
    }

    startButton.addEventListener('click', runBootSequence);
    document.addEventListener('keydown', handleNavigation);
    fetchScenes();
});
