import type { ReactNode } from 'react';

export interface LitButtonProps {
  children: ReactNode;
  /** `dark` is the near-black control on a light field; `light` is its inverse.
   *  Both wear the same rig — only the rim and the inset swap. */
  surface?: 'dark' | 'light';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

/** The pack's signature, and there is ONE per viewport. The rig is a static light:
 *  it does not change on hover, and animating it is the pack's first ban. */
export function LitButton({ children, surface = 'dark', disabled = false, onClick, className }: LitButtonProps) {
  return (
    <button
      type="button"
      className={['rl-lit', `rl-lit--${surface}`, className].filter(Boolean).join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
