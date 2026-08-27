import type { ReactNode } from 'react';

export interface DemoFrameProps {
  /** The address shown in the chrome bar — a real one; the frame quotes a live app. */
  url: string;
  /** The running interior — an iframe, or a self-narrating demo. Never a still. */
  children: ReactNode;
  className?: string;
}

export function DemoFrame({ url, children, className }: DemoFrameProps) {
  return (
    <figure className={['td-frame', className].filter(Boolean).join(' ')}>
      <div className="td-frame__chrome">
        <span className="td-frame__dots" aria-hidden="true">
          <i className="td-frame__dot td-frame__dot--red" />
          <i className="td-frame__dot td-frame__dot--amber" />
          <i className="td-frame__dot td-frame__dot--green" />
        </span>
        <span className="td-frame__url">{url}</span>
      </div>
      <div className="td-frame__window">{children}</div>
    </figure>
  );
}
