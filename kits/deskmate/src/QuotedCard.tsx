import type { ReactNode } from 'react';

export interface QuotedCardProps {
  /** The agent's own line, set on the ramp. */
  quote: string;
  title: string;
  /** The artefact the quoted line produced: a file, a link, a count. */
  artefact?: ReactNode;
  children: ReactNode;
  className?: string;
}

export function QuotedCard({ quote, title, artefact, children, className }: QuotedCardProps) {
  return (
    <section className={['dm-qcard', className].filter(Boolean).join(' ')}>
      <div className="dm-qcard__said">
        <div className="dm-qcard__byline">
          <span className="dm-qcard__author">Agent</span>
          <span className="dm-qcard__badge">APP</span>
        </div>
        <p className="dm-qcard__quote">{quote}</p>
        {artefact !== undefined && <div className="dm-qcard__artefact">{artefact}</div>}
      </div>
      <div className="dm-qcard__told">
        <h3 className="dm-qcard__title">{title}</h3>
        <div className="dm-qcard__body">{children}</div>
      </div>
    </section>
  );
}
