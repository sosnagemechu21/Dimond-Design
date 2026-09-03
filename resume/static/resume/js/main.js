/**
 * DAGIM — DIAMOND DESIGN PORTFOLIO INTERACTION ENGINE
 * 3D Orbit Physics, Stacking Cards, Lightbox Modal, and Contact Form
 */

document.addEventListener('DOMContentLoaded', () => {
    init3DOrbit();
    initStackingCards();
    initLightbox();
    initContactForm();
    initSmoothScroll();
    initFormModal();
    initQuestionnaireForms();
    initMobileNav();
    initMobileDock();
});

/* ==========================================================================
   1. 3D ORBITAL STAGE WITH DRAG-TO-SPIN & INERTIA PHYSICS (Kidus Style)
   ========================================================================== */
function init3DOrbit() {
    const stage = document.getElementById('orbit-stage');
    const center = document.getElementById('orbit-center');
    if (!stage || !center) return;

    const items = Array.from(center.querySelectorAll('.orbit-item'));
    if (items.length === 0) return;

    let currentAngle = 0;
    let velocity = 0.0035; // idle spin velocity
    let isDragging = false;
    let startX = 0;
    let previousX = 0;
    let lastDragTime = 0;
    let dragVelocity = 0;
    let isHovered = false;

    // Radius of orbit (adaptive for all screen sizes)
    let radiusX = 320;
    let radiusY = 140;

    function updateRadii() {
        const width = window.innerWidth;
        if (width < 450) {
            radiusX = Math.min(130, Math.round(width * 0.35));
            radiusY = 55;
        } else if (width < 650) {
            radiusX = 160;
            radiusY = 75;
        } else if (width < 1024) {
            radiusX = 240;
            radiusY = 100;
        } else {
            radiusX = 330;
            radiusY = 130;
        }
    }

    updateRadii();
    window.addEventListener('resize', updateRadii);

    // Distribute item initial offsets
    const totalItems = items.length;
    const baseAngles = items.map((_, i) => (i * 2 * Math.PI) / totalItems);

    function renderOrbit() {
        if (!isDragging) {
            // Apply decay to dragVelocity and return to idle velocity
            if (Math.abs(dragVelocity) > 0.0001) {
                currentAngle += dragVelocity;
                dragVelocity *= 0.94; // friction
            } else if (!isHovered) {
                currentAngle += velocity;
            }
        }

        items.forEach((item, i) => {
            const angle = baseAngles[i] + currentAngle;
            const x = Math.cos(angle) * radiusX;
            const y = Math.sin(angle) * radiusY;

            // Depth calculation: sin(angle) ranges from -1 (back) to +1 (front)
            const sinVal = Math.sin(angle);
            const normalizedDepth = (sinVal + 1) / 2; // 0 to 1

            const scale = 0.65 + normalizedDepth * 0.45; // 0.65 to 1.1
            const zIndex = Math.round(normalizedDepth * 30) + 1;
            const opacity = 0.35 + normalizedDepth * 0.65;
            const blur = (1 - normalizedDepth) * 3; // blur distant items

            item.style.transform = `translate3d(${x}px, ${y}px, 0) scale(${scale})`;
            item.style.zIndex = zIndex;
            item.style.opacity = opacity;
            item.style.filter = `blur(${blur}px)`;
        });

        requestAnimationFrame(renderOrbit);
    }

    // Touch & Pointer events for drag-to-spin with phone gesture handling
    stage.addEventListener('pointerdown', (e) => {
        isDragging = true;
        startX = e.clientX;
        previousX = e.clientX;
        lastDragTime = performance.now();
        dragVelocity = 0;
        try {
            stage.setPointerCapture(e.pointerId);
        } catch (err) {}
    });

    stage.addEventListener('pointermove', (e) => {
        if (!isDragging) return;
        const now = performance.now();
        const deltaX = e.clientX - previousX;
        const deltaTime = Math.max(now - lastDragTime, 16);

        // Convert delta pixels to radian angle (more responsive on mobile)
        const sensitivity = window.innerWidth < 600 ? 0.0075 : 0.0055;
        currentAngle += deltaX * sensitivity;
        dragVelocity = (deltaX / deltaTime) * (window.innerWidth < 600 ? 0.07 : 0.05);

        previousX = e.clientX;
        lastDragTime = now;
    });

    function endDrag(e) {
        if (!isDragging) return;
        isDragging = false;
        try {
            stage.releasePointerCapture(e.pointerId);
        } catch (err) {}
    }

    stage.addEventListener('pointerup', endDrag);
    stage.addEventListener('pointercancel', endDrag);

    // Pause idle rotation when hovering or tap interaction on phone
    items.forEach((item) => {
        item.addEventListener('mouseenter', () => (isHovered = true));
        item.addEventListener('mouseleave', () => (isHovered = false));

        // Tactile touch tap on mobile phone
        item.addEventListener('click', (e) => {
            const badge = item.querySelector('.token-badge, .token-mini, .token-pill span:last-child');
            const label = badge ? badge.textContent.trim() : 'Diamond 3D';
            showOrbitToast(label);
            // Gentle spin nudge
            dragVelocity = 0.03;
        });
    });

    renderOrbit();
}

let toastTimer = null;
function showOrbitToast(text) {
    const toast = document.getElementById('mobile-orbit-toast');
    const toastText = document.getElementById('mobile-toast-text');
    if (!toast || !toastText) return;

    toastText.textContent = text;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        toast.classList.remove('show');
    }, 2200);
}

/* ==========================================================================
   2. SIGNATURE STACKING CARDS SCROLL DYNAMICS
   ========================================================================== */
function initStackingCards() {
    const wrappers = Array.from(document.querySelectorAll('.project-sticky-wrapper'));
    if (wrappers.length === 0) return;

    function handleScroll() {
        if (window.innerWidth < 860) return; // relative on mobile

        const viewportHeight = window.innerHeight;

        wrappers.forEach((wrapper, index) => {
            const rect = wrapper.getBoundingClientRect();
            const card = wrapper.querySelector('.project-card');
            if (!card) return;

            // If the next wrapper starts overlapping this card
            if (index < wrappers.length - 1) {
                const nextWrapper = wrappers[index + 1];
                const nextRect = nextWrapper.getBoundingClientRect();

                // When next card approaches this card's top
                const overlap = rect.top - nextRect.top;
                if (nextRect.top < viewportHeight) {
                    const progress = Math.max(0, Math.min(1, (viewportHeight - nextRect.top) / viewportHeight));
                    // Subtle scale down of the card beneath
                    const scale = 1 - progress * 0.04;
                    const brightness = 1 - progress * 0.15;
                    card.style.transform = `scale(${scale})`;
                    card.style.filter = `brightness(${brightness})`;
                } else {
                    card.style.transform = 'scale(1)';
                    card.style.filter = 'brightness(1)';
                }
            }
        });
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
}

/* ==========================================================================
   3. INTERACTIVE IMAGE LIGHTBOX MODAL
   ========================================================================== */
function initLightbox() {
    const modal = document.getElementById('lightbox-modal');
    const imgEl = document.getElementById('lightbox-img');
    const titleEl = document.getElementById('lightbox-title');
    const descEl = document.getElementById('lightbox-desc');
    const closeBtn = document.getElementById('lightbox-close');
    const backdrop = modal ? modal.querySelector('.lightbox-backdrop') : null;

    if (!modal || !imgEl) return;

    function openLightbox(src, title, desc) {
        imgEl.src = src;
        imgEl.alt = title || 'Enlarged design';
        titleEl.textContent = title || '';
        descEl.textContent = desc || '';
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        setTimeout(() => {
            imgEl.src = '';
        }, 200);
    }

    document.querySelectorAll('.lightbox-trigger').forEach((trigger) => {
        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const src = trigger.dataset.img || trigger.querySelector('img')?.src;
            const title = trigger.dataset.title || '';
            const desc = trigger.dataset.desc || '';
            if (src) {
                openLightbox(src, title, desc);
            }
        });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
    if (backdrop) backdrop.addEventListener('click', closeLightbox);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeLightbox();
        }
    });
}

/* ==========================================================================
   4. AJAX CONTACT FORM
   ========================================================================== */
function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const feedback = document.getElementById('form-feedback');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.getElementById('btn-text');
    const btnSpinner = document.getElementById('btn-spinner');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Get CSRF token
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]')?.value;

        const formData = {
            name: form.querySelector('#contact-name').value.trim(),
            email: form.querySelector('#contact-email').value.trim(),
            service: form.querySelector('#contact-service').value,
            message: form.querySelector('#contact-message').value.trim(),
        };

        if (!formData.name || !formData.email || !formData.message) {
            showFeedback('Please fill in all required fields.', 'error');
            return;
        }

        // Loading state
        submitBtn.disabled = true;
        btnText.style.display = 'none';
        btnSpinner.style.display = 'inline-block';
        feedback.style.display = 'none';

        try {
            const response = await fetch('/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify(formData),
            });

            const result = await response.json();

            if (response.ok && result.status === 'success') {
                showFeedback(result.message, 'success');
                form.reset();
            } else {
                showFeedback(result.message || 'Something went wrong. Please try again.', 'error');
            }
        } catch (error) {
            showFeedback('Network error. You can also message Dagim directly on WhatsApp!', 'error');
        } finally {
            submitBtn.disabled = false;
            btnText.style.display = 'inline-block';
            btnSpinner.style.display = 'none';
        }
    });

    function showFeedback(msg, type) {
        feedback.textContent = msg;
        feedback.className = `form-feedback ${type}`;
        feedback.style.display = 'block';
    }
}

/* ==========================================================================
   5. SMOOTH SCROLL & BACK TO TOP
   ========================================================================== */
function initSmoothScroll() {
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Smooth scroll offset for fixed header
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#' || !href.startsWith('#')) return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerOffset = 70;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth',
                });
            }
        });
    });
}

/* ==========================================================================
   6. BRANDING DISCOVERY BRIEF MODAL
   ========================================================================== */
function initFormModal() {
    const modal = document.getElementById('form-modal');
    const closeBtn = document.getElementById('form-modal-close');
    const backdrop = modal ? modal.querySelector('.form-modal-backdrop') : null;
    if (!modal) return;

    function openModal() {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    document.querySelectorAll('.open-form-modal').forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            openModal();
        });
    });

    if (backdrop) backdrop.addEventListener('click', closeModal);

    // Mobile touch swipe-down to dismiss modal
    let touchStartY = 0;
    const modalBody = modal.querySelector('.form-modal-body');
    const modalHeader = modal.querySelector('.form-modal-header');

    if (modalHeader) {
        modalHeader.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
        }, { passive: true });

        modalHeader.addEventListener('touchmove', (e) => {
            if (touchStartY > 0) {
                const diff = e.touches[0].clientY - touchStartY;
                if (diff > 70) {
                    closeModal();
                    touchStartY = 0;
                }
            }
        }, { passive: true });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

/* ==========================================================================
   7. NATIVE BRANDING DISCOVERY QUESTIONNAIRE ENGINE
   ========================================================================== */
function initQuestionnaireForms() {
    const forms = document.querySelectorAll('.brand-questionnaire-form');
    if (forms.length === 0) return;

    forms.forEach((form) => {
        // 1. Interactive Aesthetic Chips
        const chipContainers = form.querySelectorAll('.q-chips-container');
        chipContainers.forEach((container) => {
            const targetInputId = container.dataset.target;
            const targetInput = form.querySelector(`#${targetInputId}`);
            const chips = container.querySelectorAll('.q-chip');

            chips.forEach((chip) => {
                chip.addEventListener('click', (e) => {
                    e.preventDefault();
                    chip.classList.toggle('active');

                    // Collect all active chip values
                    const activeValues = Array.from(container.querySelectorAll('.q-chip.active'))
                        .map((c) => c.dataset.val);

                    if (targetInput) {
                        targetInput.value = activeValues.join(', ');
                    }
                });
            });
        });

        // 2. Interactive Package Cards
        const pkgContainers = form.querySelectorAll('.q-package-grid');
        pkgContainers.forEach((container) => {
            const targetInputId = container.dataset.target;
            const targetInput = form.querySelector(`#${targetInputId}`);
            const cards = container.querySelectorAll('.q-package-card');

            cards.forEach((card) => {
                card.addEventListener('click', (e) => {
                    e.preventDefault();
                    card.classList.toggle('selected');

                    const selectedValues = Array.from(container.querySelectorAll('.q-package-card.selected'))
                        .map((c) => c.dataset.val);

                    if (targetInput) {
                        targetInput.value = selectedValues.join(', ');
                    }
                });
            });
        });

        // 3. Form Submission Handling
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const feedbackBox = form.querySelector('.q-feedback-box');
            const submitBtn = form.querySelector('.q-submit-btn');
            const btnText = form.querySelector('.q-btn-text');
            const btnSpinner = form.querySelector('.q-btn-spinner');
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]')?.value;

            // Extract all form data
            const formData = new FormData(form);
            const payload = {};
            formData.forEach((value, key) => {
                payload[key] = value;
            });

            // Basic validation
            if (!payload.full_name || !payload.email || !payload.brand_name) {
                showQuestionnaireFeedback(form, 'Please fill in all required fields (Name, Email, and Brand Name).', 'error');
                return;
            }

            // Submit loading state
            if (submitBtn) submitBtn.disabled = true;
            if (btnText) btnText.style.display = 'none';
            if (btnSpinner) btnSpinner.style.display = 'inline-block';
            if (feedbackBox) feedbackBox.style.display = 'none';

            try {
                const response = await fetch('/questionnaire/submit/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                    body: JSON.stringify(payload),
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    renderQuestionnaireSuccess(form, result);
                } else {
                    showQuestionnaireFeedback(form, result.message || 'Unable to submit brief. Please check your inputs.', 'error');
                }
            } catch (err) {
                showQuestionnaireFeedback(form, 'Network connection issue. You can also chat directly with Dagim on WhatsApp!', 'error');
            } finally {
                if (submitBtn) submitBtn.disabled = false;
                if (btnText) btnText.style.display = 'inline-block';
                if (btnSpinner) btnSpinner.style.display = 'none';
            }
        });
    });

    function showQuestionnaireFeedback(form, message, type) {
        const box = form.querySelector('.q-feedback-box');
        if (!box) return;
        box.className = `q-feedback-box ${type}`;
        box.innerHTML = `<p>${message}</p>`;
        box.style.display = 'block';
        box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function renderQuestionnaireSuccess(form, result) {
        const box = form.querySelector('.q-feedback-box');
        if (!box) return;

        // Hide form input blocks and action buttons
        const blocks = form.querySelectorAll('.q-block, .q-actions-row');
        blocks.forEach((el) => (el.style.display = 'none'));

        box.className = 'q-feedback-box success';
        box.innerHTML = `
            <div class="q-success-inner">
                <div class="q-success-icon">✦</div>
                <h3 class="q-success-title">Discovery Brief Received!</h3>
                <p class="q-success-msg">${result.message}</p>
                <div class="q-success-actions">
                    <a href="${result.whatsapp_link}" target="_blank" rel="noopener noreferrer" class="btn-whatsapp-direct">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path>
                        </svg>
                        <span>Notify Dagim on WhatsApp Now</span>
                    </a>
                    <button type="button" class="btn-outline-pill btn-md btn-reset-brief">
                        <span>Submit Another Brief</span>
                    </button>
                </div>
            </div>
        `;
        box.style.display = 'block';
        box.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Wire reset button
        const resetBtn = box.querySelector('.btn-reset-brief');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                form.reset();
                // Reset chip & package active states
                form.querySelectorAll('.q-chip.active').forEach((c) => c.classList.remove('active'));
                form.querySelectorAll('.q-package-card.selected').forEach((c, idx) => {
                    if (idx !== 0) c.classList.remove('selected');
                });
                blocks.forEach((el) => (el.style.display = ''));
                box.style.display = 'none';
            });
        }
    }
}

/* ==========================================================================
   8. MOBILE PHONE NAVIGATION DRAWER
   ========================================================================== */
function initMobileNav() {
    const toggle = document.getElementById('mobile-menu-toggle');
    const drawer = document.getElementById('mobile-nav-drawer');
    const closeBtn = document.getElementById('mobile-drawer-close');
    const backdrop = document.getElementById('mobile-drawer-backdrop');
    if (!toggle || !drawer) return;

    function openDrawer() {
        drawer.classList.add('active');
        toggle.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
        drawer.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
        drawer.classList.remove('active');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        drawer.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        if (drawer.classList.contains('active')) {
            closeDrawer();
        } else {
            openDrawer();
        }
    });

    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (backdrop) backdrop.addEventListener('click', closeDrawer);

    // Close when tapping any navigation link and scroll smoothly
    drawer.querySelectorAll('.mobile-nav-link').forEach((link) => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            closeDrawer();

            if (href && href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const headerOffset = 65;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth',
                    });
                }
            }
        });
    });

    // Close when tapping CTA button in drawer
    drawer.querySelectorAll('.mobile-drawer-cta').forEach((btn) => {
        btn.addEventListener('click', () => {
            closeDrawer();
        });
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && drawer.classList.contains('active')) {
            closeDrawer();
        }
    });
}

/* ==========================================================================
   9. MOBILE FLOATING ACTION DOCK
   ========================================================================== */
function initMobileDock() {
    const dock = document.getElementById('mobile-bottom-dock');
    if (!dock) return;

    let lastScrollY = window.pageYOffset;
    let isHidden = false;

    window.addEventListener('scroll', () => {
        const currentScrollY = window.pageYOffset;
        const diff = currentScrollY - lastScrollY;

        // Hide when scrolling down quickly, reappear on scroll up or top of page
        if (diff > 14 && currentScrollY > 180) {
            if (!isHidden) {
                dock.classList.add('dock-hidden');
                isHidden = true;
            }
        } else if (diff < -8 || currentScrollY < 100) {
            if (isHidden) {
                dock.classList.remove('dock-hidden');
                isHidden = false;
            }
        }

        lastScrollY = currentScrollY;
    }, { passive: true });
}


