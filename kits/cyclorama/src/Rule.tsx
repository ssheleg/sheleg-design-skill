export interface RuleProps {
  tone?: 'hairline' | 'strong';
  className?: string;
}

/**
 * `hairline` is `--line-soft`, `strong` is `--line`. Both are the same 1px
 * rule at different alphas — this pack has no thicker divider and no shadow to
 * separate anything with, so a rule is the only separator that exists.
 *
 * Note that a rule reads differently here than in a ruled pack like
 * `field-notes`: there the hairline *composes* the page, here it is furniture
 * inside a panel. Do not build a page out of these.
 */
export function Rule({ tone = 'hairline', className }: RuleProps) {
  return (
    <hr
      className={[
        'cy-rule',
        tone === 'strong' ? 'cy-rule--strong' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    />
  );
}
