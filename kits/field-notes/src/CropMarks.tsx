export interface CropMarksProps {
  className?: string;
}

/**
 * Printer's registration marks: eight 1px arms at the four corners of whatever
 * positioned box contains them, ink at 30%, desktop only. They cost nothing and
 * they state the thesis — this page was printed and trimmed.
 *
 * Drop one inside a `position: relative` container. Below `48rem` they are
 * hidden, so they never become a touch target. On the dawn — the only dark
 * surface in the pack — pass `className="fn-crop--on-deep"`.
 */
export function CropMarks({ className }: CropMarksProps) {
  return (
    <span aria-hidden="true" className={['fn-crop', className].filter(Boolean).join(' ')} />
  );
}
