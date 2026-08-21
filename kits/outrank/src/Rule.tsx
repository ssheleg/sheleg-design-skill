import type { ReactNode } from 'react';

export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return <hr className={['or-rule', tone === 'strong' ? 'or-rule--strong' : undefined, className].filter(Boolean).join(' ')} />;
}
