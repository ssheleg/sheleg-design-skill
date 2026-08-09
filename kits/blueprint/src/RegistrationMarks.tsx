import type { ReactNode } from 'react';

export interface RegistrationMarksProps {
  /** `accent` puts the marks in the pack's blue; `grid` keeps them faint. */
  tone?: 'grid' | 'accent';
  children: ReactNode;
  className?: string;
}

/**
 * Four L-shaped brackets at the corners of whatever it wraps: 8px arms at 1px,
 * offset 6px from the object they register.
 *
 * They are the pack's signature and they must stay rare. A registration mark
 * exists so two plates line up in a press — it is a mark about *accuracy*, made
 * by someone who assumed you would recognise it. Put them on **one** thing per
 * viewport: the action the page wants, or the figure it is arguing from. Marks
 * on every card is a texture; marks on the one thing that matters is an
 * argument.
 *
 * Desktop only. At 8px they become touch-target confetti on a phone, so they
 * come off buttons below 768px and stay only on framed figures.
 */
export function RegistrationMarks({ tone = 'grid', children, className }: RegistrationMarksProps) {
  return (
    <span className={['bp-reg', `bp-reg--${tone}`, className].filter(Boolean).join(' ')}>
      {children}
      <i className="bp-reg__tick bp-reg__tick--tl" aria-hidden="true" />
      <i className="bp-reg__tick bp-reg__tick--tr" aria-hidden="true" />
      <i className="bp-reg__tick bp-reg__tick--bl" aria-hidden="true" />
      <i className="bp-reg__tick bp-reg__tick--br" aria-hidden="true" />
    </span>
  );
}
