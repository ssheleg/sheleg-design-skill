import type { ReactNode } from 'react';

export interface DialogueProps {
  /** The teal Q glyph and the question. */
  question: string;
  /** The pink A glyph and the answer body. */
  children: ReactNode;
  className?: string;
}

export function Dialogue({ question, children, className }: DialogueProps) {
  return (
    <div className={['sv-dialogue', className].filter(Boolean).join(' ')}>
      <div className="sv-dialogue__q">
        <span className="sv-dialogue__glyph sv-dialogue__glyph--q" aria-hidden="true">Q</span>
        <h3 className="sv-dialogue__question">{question}</h3>
      </div>
      <div className="sv-dialogue__a">
        <span className="sv-dialogue__glyph sv-dialogue__glyph--a" aria-hidden="true">A</span>
        <div className="sv-dialogue__answer">{children}</div>
      </div>
    </div>
  );
}
