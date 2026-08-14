import type { ReactNode } from 'react';

export interface LatticeCellProps {
  index: string;
  title: string;
  /** One sentence in the 32ch measure. */
  children?: ReactNode;
  /** `invert` flips the cell to solid on hover — the pack's only hover fill. */
  invert?: boolean;
  className?: string;
}

/**
 * A cell in the hairline lattice. It draws its OWN right and bottom border and
 * the container draws top and left, which is why a cell can go solid on hover
 * without a seam appearing along its edge.
 *
 * The title is pushed to the bottom with margin-top: auto, so a row of cells
 * with different amounts of copy still aligns on its titles.
 */
export function LatticeCell({ index, title, children, invert = true, className }: LatticeCellProps) {
  return (
    <article
      className={[
        'tn-cell',
        invert ? 'tn-cell--invert' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <span className="tn-cell__index">{index}</span>
      <h3 className="tn-cell__title">{title}</h3>
      {children !== undefined && <p className="tn-cell__body">{children}</p>}
    </article>
  );
}
