export type Severity = 'ask' | 'limit' | 'never';

export interface GuardrailProps {
  severity: Severity;
  /** The chip's word. Required: severity is value here, and value needs a word. */
  label: string;
  /** What the rule applies to. */
  children: string;
  className?: string;
}

/**
 * The pack's status primitive, and the proof that severity is value rather than
 * hue: `ask` is the orange, `limit` is the deep paper, `never` is the ink.
 *
 * `label` is a required prop for the same reason the palette says status is
 * never by colour alone — the orange sits at 3.02:1 on the paper and cannot
 * carry a meaning by itself.
 */
export function Guardrail({ severity, label, children, className }: GuardrailProps) {
  return (
    <p className={['tn-guard', `tn-guard--${severity}`, className].filter(Boolean).join(' ')}>
      <span className="tn-guard__chip">{label}</span>
      <span className="tn-guard__text">{children}</span>
    </p>
  );
}
