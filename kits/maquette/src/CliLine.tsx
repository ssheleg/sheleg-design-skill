export interface CliLineProps {
  command: string;
  /** The words before the command — "Build with CLI". */
  label?: string;
  onCopy?: () => void;
  copied?: boolean;
  className?: string;
}

/**
 * The enterprise page that still shows you a command: `--surface-sunken` on a
 * 1px `--line`, the label in `--ink-soft` and the command in `--ink`, both mono.
 *
 * The copy control changes its **label**, not only its colour — the same rule
 * as the status marks, and for the same readers.
 */
export function CliLine({ command, label, onCopy, copied = false, className }: CliLineProps) {
  return (
    <div className={['mq-cli', className].filter(Boolean).join(' ')}>
      {label !== undefined && <span className="mq-cli__label">{label}</span>}
      <code className="mq-cli__cmd">{command}</code>
      <button type="button" className="mq-cli__copy" onClick={onCopy}>
        {copied ? 'copied' : 'copy'}
      </button>
    </div>
  );
}
