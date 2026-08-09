import type { ReactNode } from 'react';

export interface ModelBlockProps {
  /** The block's name. An unlabelled block is decoration — remove it instead. */
  label: string;
  /** Depth in the stack, 1 = the substrate. Controls only the z-order. */
  tier?: 1 | 2 | 3;
  children?: ReactNode;
  className?: string;
}

/**
 * One cream solid of the axonometric model: three flat faces
 * (`--model-top`, `--model-face`, `--model-side`) separated by `--model-line`,
 * which is the field colour itself — so the blocks are divided by the table
 * showing between them rather than by a drawn stroke.
 *
 * **Axonometric, never perspective.** No vanishing point, so every block keeps
 * its true proportion and the drawing stays measurable. A perspective render
 * says *look at this*; an axonometric drawing says *check this*, and that is the
 * question an architecture buyer is asking.
 *
 * **It does not move.** No parallax, no rotation, no exploded view on scroll, no
 * hover highlight. A measurable object that drifts stops being measurable.
 */
export function ModelBlock({ label, tier = 1, children, className }: ModelBlockProps) {
  return (
    <div
      className={['mq-block', `mq-block--t${tier}`, className].filter(Boolean).join(' ')}
      data-label={label}
    >
      <span className="mq-block__top" aria-hidden="true" />
      <span className="mq-block__face" aria-hidden="true" />
      <span className="mq-block__side" aria-hidden="true" />
      <span className="mq-block__label">{label}</span>
      {children}
    </div>
  );
}
