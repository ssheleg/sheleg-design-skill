import type { ReactNode } from 'react';

export interface TranscriptProps {
  /** The channel the conversation happens in, drawn in the client's own chrome. */
  channel: string;
  /** Which client is being quoted — it labels the frame, it does not restyle it. */
  client?: 'slack' | 'teams' | 'generic';
  children: ReactNode;
  className?: string;
}

export function Transcript({ channel, client = 'generic', children, className }: TranscriptProps) {
  return (
    <figure className={['dm-frame', className].filter(Boolean).join(' ')}>
      <div className="dm-frame__window">
        <div className="dm-frame__bar">
          <span className="dm-frame__channel">#&nbsp;{channel}</span>
          <span className="dm-frame__client">{client}</span>
        </div>
        <div className="dm-frame__body">{children}</div>
      </div>
    </figure>
  );
}
