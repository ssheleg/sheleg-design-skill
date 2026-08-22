export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return <hr className={['pb-rule', `pb-rule--${tone}`, className].filter(Boolean).join(' ')} />;
}
