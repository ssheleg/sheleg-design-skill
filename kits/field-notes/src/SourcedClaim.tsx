import type { ReactNode } from 'react';
import { ProvenanceTag } from './ProvenanceTag.js';
import type { Provenance } from './ProvenanceTag.js';

export interface SourcedClaimProps {
  /** The claim. A sentence that argues, not a feature name. */
  children: ReactNode;
  /**
   * Who produced it — the run, the paper, the query, the person. **Required**:
   * a claim with no source in the same block is a ban in this pack, so it is
   * not a prop you can forget.
   */
  source: string;
  /** Renders a `ProvenanceTag` inline, right after the claim. */
  provenance?: Provenance;
  className?: string;
}

/**
 * A claim with its evidence attached, in one block. The source is not a
 * footnote, not a superscript and not a tooltip: on a pack whose product is
 * provenance, the attribution *is* the argument, and moving it to the bottom of
 * the page is how a provenance product stops being one.
 */
export function SourcedClaim({ children, source, provenance, className }: SourcedClaimProps) {
  return (
    <figure className={['fn-claim', className].filter(Boolean).join(' ')}>
      <p className="fn-claim__body">
        {children}
        {provenance !== undefined && (
          <ProvenanceTag state={provenance} className="fn-claim__tag" />
        )}
      </p>
      <figcaption>
        <cite className="fn-claim__source">{source}</cite>
      </figcaption>
    </figure>
  );
}
