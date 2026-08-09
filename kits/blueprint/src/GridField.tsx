export interface GridFieldProps {
  /** Dot spacing in px. Halves below 768px so density stays visually constant. */
  step?: number;
  className?: string;
}

/**
 * The drawing grid: 1px dots in `--line-grid` at `--grid-step`.
 *
 * It sits at depth layer 1 — `pointer-events: none`, `aria-hidden`, behind
 * everything, never on a scroller. **It never animates**: not on load, not on
 * scroll, not on hover. It is the sheet the page is drawn on, and a sheet that
 * moves is a different kind of page.
 */
export function GridField({ step, className }: GridFieldProps) {
  return (
    <div
      className={['bp-grid', className].filter(Boolean).join(' ')}
      style={step !== undefined ? ({ ['--grid-step' as string]: `${step}px` } as object) : undefined}
      aria-hidden="true"
    />
  );
}
