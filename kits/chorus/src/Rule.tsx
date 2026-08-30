export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={['ch-rule', `ch-rule--${tone}`, className].filter(Boolean).join(' ')}
    />
  );
}
