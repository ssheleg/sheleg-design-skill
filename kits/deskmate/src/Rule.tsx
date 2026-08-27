export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'dm-rule',
        tone === 'strong' ? 'dm-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
