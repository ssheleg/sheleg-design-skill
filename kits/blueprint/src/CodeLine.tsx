export interface CodeLineProps {
  command: string;
  /** Shown before the command, in --ink-faint. Defaults to a shell prompt. */
  prompt?: string;
  onCopy?: () => void;
  /** Flipped by the caller after a copy. Changes the LABEL, not just a colour. */
  copied?: boolean;
  className?: string;
}

/**
 * A command in JetBrains Mono on `--surface-2`, zero radius, with a copy
 * control at the right.
 *
 * The copy control changes its **label** to `copied`, not only its colour — the
 * same rule the pack applies to category marks, and for the same readers.
 */
export function CodeLine({ command, prompt = '$', onCopy, copied = false, className }: CodeLineProps) {
  return (
    <div className={['bp-code', className].filter(Boolean).join(' ')}>
      <span className="bp-code__prompt" aria-hidden="true">{prompt}</span>
      <code className="bp-code__cmd">{command}</code>
      <button type="button" className="bp-code__copy" onClick={onCopy}>
        {copied ? 'copied' : 'copy'}
      </button>
    </div>
  );
}
