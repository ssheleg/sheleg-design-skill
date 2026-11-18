export interface PromptProps {
  /** The chapter number, set as `[ CH 03 ]`. */
  chapter?: string;
  children: string;
  /** Type the line on in 24 steps when it mounts. */
  typed?: boolean;
  className?: string;
}

/** A mono headline with the terminal prompt: `> ` before it, a bracketed chapter above it. */
export function Prompt({ chapter, children, typed = false, className }: PromptProps) {
  return (
    <div className={['ph-prompt', typed ? 'ph-prompt--typed' : null, className].filter(Boolean).join(' ')}>
      {chapter && <span className="ph-prompt__chapter">{chapter}</span>}
      <h2 className="ph-prompt__line">{children}</h2>
    </div>
  );
}
