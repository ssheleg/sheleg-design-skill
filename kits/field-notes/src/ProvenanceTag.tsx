/**
 * The three epistemic states of a claim. There is no fourth, and there is no
 * confidence percentage — a number pretending to be a probability is exactly
 * what this tag exists instead of.
 */
export type Provenance = 'extracted' | 'inferred' | 'ambiguous';

export interface ProvenanceTagProps {
  state: Provenance;
  className?: string;
}

const LABEL: Record<Provenance, string> = {
  extracted: '[EXTRACTED]',
  inferred: '[INFERRED]',
  ambiguous: '[AMBIGUOUS]',
};

/**
 * `[EXTRACTED]` · `[INFERRED]` · `[AMBIGUOUS]` — bracketed mono at 10px and
 * `0.08em`, transparent fill, a 1px border of the state's own ink at 25% alpha.
 *
 * **It sits inline with the claim it qualifies, never in a legend.** A legend
 * moves the reader away from the sentence to find out how the sentence is
 * known, which is the opposite of what the pack is for; the tag has to be
 * readable in the same glance as the words it marks.
 */
export function ProvenanceTag({ state, className }: ProvenanceTagProps) {
  return (
    <span className={['fn-prov', `fn-prov--${state}`, className].filter(Boolean).join(' ')}>
      {LABEL[state]}
    </span>
  );
}
