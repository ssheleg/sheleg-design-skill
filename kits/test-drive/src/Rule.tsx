export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'td-rule',
        tone === 'strong' ? 'td-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
