import type { ReactNode } from 'react';

export interface FrameProps {
  caption?: string;
  /** The honesty line under the panel: what this view is drawn from. */
  foot?: string;
  /** The fold cuts the panel off — the pack's signature. See Frame.md. */
  cropped?: boolean;
  children: ReactNode;
  className?: string;
}

export function Frame({ caption, foot, cropped = false, children, className }: FrameProps) {
  return (
    <figure
      className={['ps-frame', cropped ? 'ps-frame--cropped' : undefined, className]
        .filter(Boolean)
        .join(' ')}
    >
      {caption !== undefined && <figcaption className="ps-frame__cap">{caption}</figcaption>}
      <div className="ps-frame__glass">{children}</div>
      {foot !== undefined && !cropped && <p className="ps-frame__foot">{foot}</p>}
    </figure>
  );
}
