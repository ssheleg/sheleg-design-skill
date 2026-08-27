import type { ReactNode } from 'react';

export interface MessageProps {
  author: string;
  /** `app` marks the agent's own turn and draws the APP badge beside the name. */
  kind?: 'person' | 'app';
  time?: string;
  children: ReactNode;
  className?: string;
}

export function Message({ author, kind = 'person', time, children, className }: MessageProps) {
  return (
    <article className={['dm-msg', `dm-msg--${kind}`, className].filter(Boolean).join(' ')}>
      <div className="dm-msg__byline">
        <span className="dm-msg__author">{author}</span>
        {kind === 'app' && <span className="dm-msg__badge">APP</span>}
        {time !== undefined && <span className="dm-msg__time">{time}</span>}
      </div>
      <div className="dm-msg__body">{children}</div>
    </article>
  );
}
