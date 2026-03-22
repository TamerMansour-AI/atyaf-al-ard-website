(() => {
  const roots = Array.from(document.querySelectorAll('[data-browse-root]'));
  if (!roots.length) return;
  const tokens = (value) => String(value || '').split('|').map((item) => item.trim()).filter(Boolean);
  roots.forEach((root) => {
    const items = Array.from(root.querySelectorAll('[data-browse-item]'));
    const controls = Array.from(root.querySelectorAll('[data-filter-key]'));
    const count = root.querySelector('[data-browse-count]');
    const empty = root.querySelector('[data-browse-empty]');
    const clear = root.querySelector('[data-clear-filters]');
    const update = () => {
      let visible = 0;
      items.forEach((item) => {
        const match = controls.every((control) => {
          if (!control.value) return true;
          return tokens(item.dataset[control.dataset.filterKey] || '').includes(control.value);
        });
        item.hidden = !match;
        if (match) visible += 1;
      });
      if (count) count.textContent = `${visible} result${visible === 1 ? '' : 's'}`;
      if (empty) empty.hidden = visible !== 0;
    };
    controls.forEach((control) => control.addEventListener('change', update));
    if (clear) clear.addEventListener('click', () => { controls.forEach((control) => { control.value = ''; }); update(); });
    update();
  });
})();
