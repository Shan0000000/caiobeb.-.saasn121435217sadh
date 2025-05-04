// Notebook toggle
document.getElementById('notebookCover').addEventListener('click', () => {
    document.getElementById('notebook').classList.toggle('open');
  });
  
  // Particles
  const canvas = document.getElementById('particles');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  let particles = [];
  for (let i = 0; i < 80; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      radius: Math.random() * 1.8 + 0.8,
      speed: Math.random() * 0.5 + 0.2,
      color: `rgba(255,255,255,${Math.random() * 0.8})`
    });
  }
  
  function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let p of particles) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, 2 * Math.PI);
      ctx.fillStyle = p.color;
      ctx.fill();
      p.y -= p.speed;
      if (p.y < -5) {
        p.y = canvas.height + 5;
        p.x = Math.random() * canvas.width;
      }
    }
    requestAnimationFrame(animateParticles);
  }
  animateParticles();
  