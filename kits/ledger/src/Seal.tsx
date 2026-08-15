export type SealState = 'verified' | 'inferred' | 'unverified';

export interface SealProps {
  state: SealState;
  /** Overrides the default word. Keep it one word: this sits in a title row. */
  label?: string;
  /** Where the reader checks it — the metric definition, the query, the source row. */
  href?: string;
  className?: string;
}

const DEFAULT_LABEL: Record<SealState, string> = {
  verified: 'Verified',
  inferred: 'Inferred',
  unverified: 'Unverified',
};

export function Seal({ state, label, href, className }: SealProps) {
  const word = label ?? DEFAULT_LABEL[state];
  const body = (
    <>
      <span className="lg-seal__glyph" aria-hidden="true" />
      <span className="lg-seal__word">{word}</span>
    </>
  );
  const classes = ['lg-seal', `lg-seal--${state}`, className].filter(Boolean).join(' ');
  return href === undefined ? (
    <span className={classes}>{body}</span>
  ) : (
    <a className={classes} href={href}>
      {body}
    </a>
  );
}
