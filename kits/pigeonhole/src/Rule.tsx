export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'pg-rule',
        tone === 'strong' ? 'pg-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
