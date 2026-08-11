export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'sb-rule',
        tone === 'strong' ? 'sb-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
