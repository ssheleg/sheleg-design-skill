import type { ReactNode } from 'react';

export interface BalloonProps {
  /** Speaker label, mono caps above the line. */
  who?: string;
  /** Which side the tail points to: the speaker's side. */
  side?: 'left' | 'right';
  /** A portrait or a Duotone beside the balloon. */
  avatar?: ReactNode;
  children: ReactNode;
  className?: string;
}

export function Balloon({ who, side = 'left', avatar, children, className }: BalloonProps) {
  return (
    <div className={['ph-say', side === 'right' ? 'ph-say--right' : null, className].filter(Boolean).join(' ')}>
      {avatar}
      <div className="ph-balloon">
        {who && <span className="ph-balloon__who">{who}</span>}
        <p className="ph-balloon__text">{children}</p>
      </div>
    </div>
  );
}
