export interface RuleProps {
  /** `hairline` goes between rows; `strong` goes around a control. */
  tone?: 'hairline' | 'strong';
  className?: string;
}

export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={['aw-rule', tone === 'strong' ? 'aw-rule--strong' : undefined, className]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
