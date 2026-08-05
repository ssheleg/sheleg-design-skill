export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={['br-rule', tone === 'strong' ? 'br-rule--strong' : undefined, className]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
