export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'tn-rule',
        tone === 'strong' ? 'tn-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
