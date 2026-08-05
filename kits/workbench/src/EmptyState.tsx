import { Button } from './Button.js';

export interface EmptyStateProps {
  /** One dim sentence. Say what is absent and why, not "No data". */
  message: string;
  /** The single way out. Omit both action props when there is no action. */
  actionLabel?: string;
  onAction?: () => void;
  className?: string;
}

export function EmptyState({ message, actionLabel, onAction, className }: EmptyStateProps) {
  return (
    <div className={['wb-empty', className].filter(Boolean).join(' ')}>
      <p className="wb-empty__message">{message}</p>
      {actionLabel !== undefined && (
        <Button variant="secondary" size="sm" onClick={onAction}>
          {actionLabel}
        </Button>
      )}
    </div>
  );
}
