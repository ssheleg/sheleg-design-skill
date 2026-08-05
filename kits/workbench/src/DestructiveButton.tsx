import { useState } from 'react';
import type { ReactNode } from 'react';

export interface DestructiveButtonProps {
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  /** What the first click swaps the label to. The second click fires `onClick`. */
  confirmLabel?: string;
  className?: string;
}

/**
 * The pack's third button: a red-border ghost that asks once before it fires.
 * The confirm step lives here rather than in the caller, so no screen can ship
 * a destructive action that skipped it.
 */
export function DestructiveButton({
  children,
  onClick,
  disabled = false,
  confirmLabel = 'Confirm',
  className,
}: DestructiveButtonProps) {
  const [armed, setArmed] = useState(false);

  return (
    <button
      type="button"
      className={[
        'wb-btn',
        'wb-btn--md',
        'wb-btn--destructive',
        armed ? 'wb-btn--armed' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={() => {
        if (armed) {
          setArmed(false);
          onClick?.();
          return;
        }
        setArmed(true);
      }}
      // Leaving the wrong button armed behind you is the failure this component
      // exists to prevent, so looking away disarms it. No timer, no animation.
      onBlur={() => setArmed(false)}
    >
      {armed ? confirmLabel : children}
    </button>
  );
}
