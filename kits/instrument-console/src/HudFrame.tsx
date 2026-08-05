import type { ReactNode } from 'react';

export interface HudFrameProps {
  /** Mono caption set into the top-left of the frame. */
  label?: string;
  children: ReactNode;
  className?: string;
}

export function HudFrame({ label, children, className }: HudFrameProps) {
  return (
    <div className={['ic-hud', className].filter(Boolean).join(' ')}>
      <span className="ic-hud__tick ic-hud__tick--tl" aria-hidden="true" />
      <span className="ic-hud__tick ic-hud__tick--tr" aria-hidden="true" />
      <span className="ic-hud__tick ic-hud__tick--bl" aria-hidden="true" />
      <span className="ic-hud__tick ic-hud__tick--br" aria-hidden="true" />
      {label !== undefined && <span className="ic-hud__label">{label}</span>}
      <div className="ic-hud__body">{children}</div>
    </div>
  );
}
