import type { ReactNode } from 'react';

export interface ItalicAsideProps {
  children: ReactNode;
  className?: string;
}

/**
 * The pack's entire emphasis vocabulary: one phrase inside a serif headline
 * turned italic and terracotta. It inherits the headline's family, size and
 * 300 weight — it is the same sentence changing its mind, not a second style.
 * One per heading, never two in a viewport.
 */
export function ItalicAside({ children, className }: ItalicAsideProps) {
  return <em className={['at-aside', className].filter(Boolean).join(' ')}>{children}</em>;
}
