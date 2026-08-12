import type { ReactNode } from 'react';

export interface CodeFrameProps {
  /** The filename in the header row — `zernio.ts`, `main.py`. */
  filename: string;
  /** The language label on the right of the header row. */
  language?: string;
  /** Rendered as-is; highlight upstream. Never reflowed, never resized. */
  children: ReactNode;
  className?: string;
}

export function CodeFrame({ filename, language, children, className }: CodeFrameProps) {
  return (
    <figure className={['mp-code', className].filter(Boolean).join(' ')}>
      <figcaption className="mp-code__head">
        <span className="mp-code__dots" aria-hidden="true">
          <i /><i /><i />
        </span>
        <span className="mp-code__name">{filename}</span>
        {language !== undefined && <span className="mp-code__lang">{language}</span>}
      </figcaption>
      <pre className="mp-code__body"><code>{children}</code></pre>
    </figure>
  );
}
