import type { ReactNode } from 'react';

export interface TerminalProps {
  /** The strip above the body: TERMINAL, RESPONSE, a path. Rendered uppercase. */
  label?: string;
  /** Right-hand affordance on the label strip, usually a copy control. */
  action?: ReactNode;
  /** Raw machine output. Whitespace is preserved; overflow scrolls in the block. */
  children: ReactNode;
  className?: string;
}

/**
 * The one surface that goes below the page plane. It never carries a shadow: a
 * block of machine output is cut into the field, not raised off it.
 */
export function Terminal({ label = 'terminal', action, children, className }: TerminalProps) {
  return (
    <div className={['ora-terminal', className].filter(Boolean).join(' ')}>
      <div className="ora-terminal__bar">
        <span className="ora-terminal__label">{label}</span>
        {action !== undefined && <span className="ora-terminal__action">{action}</span>}
      </div>
      <pre className="ora-terminal__body">{children}</pre>
    </div>
  );
}
