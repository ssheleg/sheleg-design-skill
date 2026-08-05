import type { ReactNode } from 'react';

export interface HighlightPhraseProps {
  children: ReactNode;
  className?: string;
}

/**
 * The accent-filled marker behind the one sentence fragment the whole story
 * hangs on. **Once per deck** — see HighlightPhrase.md.
 */
export function HighlightPhrase({ children, className }: HighlightPhraseProps) {
  return (
    <mark className={['br-highlight', className].filter(Boolean).join(' ')}>{children}</mark>
  );
}
