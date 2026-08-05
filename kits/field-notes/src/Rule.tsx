export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

/**
 * The hairline that does this pack's composition. A section divided by one line
 * **is** this component — pass `className="fn-rule--section"` for the 64px
 * section rhythm. There is deliberately no `RuledSheet`: a second name for the
 * same thing is how a token interface rots.
 */
export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'fn-rule',
        tone === 'strong' ? 'fn-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
