import type { ReactNode } from 'react';

export interface FrameProps {
  caption?: string;
  /** The honesty line under the case: what this specimen is, and is not. */
  foot?: string;
  children: ReactNode;
  className?: string;
}

export function Frame({ caption, foot, children, className }: FrameProps) {
  return (
    <figure className={['vt-frame', className].filter(Boolean).join(' ')}>
      {caption !== undefined && <figcaption className="vt-frame__cap">{caption}</figcaption>}
      <div className="vt-frame__glass">{children}</div>
      {foot !== undefined && <p className="vt-frame__foot">{foot}</p>}
    </figure>
  );
}
