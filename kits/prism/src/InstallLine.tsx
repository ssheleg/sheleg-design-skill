export interface InstallLineProps {
  command: string;
  prompt?: string;
  onCopy?: () => void;
  /** Flipped by the caller after a copy. Changes the LABEL, not just a colour. */
  copied?: boolean;
  className?: string;
}

/**
 * The command, in the first viewport.
 *
 * A developer who has to scroll to find how to start has already left, so this
 * belongs above the fold — not below it, not behind a tab. It is the last
 * element to be compromised at any breakpoint.
 *
 * The copy control changes its **label** to `copied`, not only its colour.
 */
export function InstallLine({ command, prompt = '$', onCopy, copied = false, className }: InstallLineProps) {
  return (
    <div className={['pr-install', className].filter(Boolean).join(' ')}>
      <span className="pr-install__prompt" aria-hidden="true">{prompt}</span>
      <code className="pr-install__cmd">{command}</code>
      <button type="button" className="pr-install__copy" onClick={onCopy}>
        {copied ? 'copied' : 'copy'}
      </button>
    </div>
  );
}
