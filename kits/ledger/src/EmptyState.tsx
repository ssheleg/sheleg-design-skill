import { Button } from './Button.js';

export interface EmptyStateProps {
  /** One dim sentence. Say what this surface can answer, not "No data". */
  message: string;
  /** Two or three real questions. Clicking one runs it — examples are affordances. */
  examples?: string[];
  onExample?: (example: string) => void;
  actionLabel?: string;
  onAction?: () => void;
  className?: string;
}

export function EmptyState({
  message,
  examples,
  onExample,
  actionLabel,
  onAction,
  className,
}: EmptyStateProps) {
  return (
    <div className={['lg-empty', className].filter(Boolean).join(' ')}>
      <p className="lg-empty__message">{message}</p>
      {examples !== undefined && examples.length > 0 && (
        <ul className="lg-empty__examples">
          {examples.map((example) => (
            <li key={example}>
              <button
                type="button"
                className="lg-empty__example"
                onClick={() => onExample?.(example)}
              >
                {example}
              </button>
            </li>
          ))}
        </ul>
      )}
      {actionLabel !== undefined && (
        <Button variant="secondary" size="sm" onClick={onAction}>
          {actionLabel}
        </Button>
      )}
    </div>
  );
}
