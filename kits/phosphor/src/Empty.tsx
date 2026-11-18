export interface EmptyProps {
  /** The prompt line, in mono after a `>`. */
  prompt: string;
  /** One sentence on what fills this place, and how. */
  children?: string;
  className?: string;
}

/** The empty state: a dashed cell, a prompt line, one sentence. No illustration. */
export function Empty({ prompt, children, className }: EmptyProps) {
  return (
    <div className={['ph-empty', className].filter(Boolean).join(' ')}>
      <p className="ph-empty__prompt">{prompt}</p>
      {children && <p className="ph-empty__text">{children}</p>}
    </div>
  );
}
