import type { ReactNode } from 'react';

export interface ClaimTitleProps {
  /** `slide` is the 64px headline; `cover` is the 128px display for slide one. */
  size?: 'slide' | 'cover';
  children: ReactNode;
  className?: string;
}

/**
 * The slide's headline, and it renders a claim rather than a label — see
 * ClaimTitle.md. Always an `h2`: the frame around it is the section.
 */
export function ClaimTitle({ size = 'slide', children, className }: ClaimTitleProps) {
  return (
    <h2 className={['br-claim', `br-claim--${size}`, className].filter(Boolean).join(' ')}>
      {children}
    </h2>
  );
}
