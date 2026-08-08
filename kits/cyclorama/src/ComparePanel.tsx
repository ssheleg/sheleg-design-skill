import type { ReactNode } from 'react';

export interface CompareRow {
  /** The dimension being compared — the row's label. */
  dimension: string;
  /** The unmarked side: what happens without the product. */
  without: string;
  /** The marked side. Always rendered with its mark AND its words. */
  with: string;
}

export interface ComparePanelProps {
  rows: CompareRow[];
  /** Column headings. Defaults to no header row at all. */
  headings?: [string, string];
  children?: ReactNode;
  className?: string;
}

/**
 * The mist panel — the one place below the hero where a real fill appears.
 * `--panel` at `--radius-lg`, hairline rows, and one mark per row on the
 * marked side.
 *
 * Ink measures 9.76:1 on `--panel`, so the panel is safe for body copy; it is
 * the only surface in the pack besides `--surface` that is.
 *
 * The marked side always carries its phrase. A column of bare accent dots is a
 * legend a reader with protanopia cannot use — see `StatusPill` for the
 * measurements — and it is also just worse writing.
 */
export function ComparePanel({ rows, headings, children, className }: ComparePanelProps) {
  return (
    <section className={['cy-compare', className].filter(Boolean).join(' ')}>
      <table className="cy-compare__table">
        {headings !== undefined && (
          <thead>
            <tr>
              <th />
              <th>{headings[0]}</th>
              <th>{headings[1]}</th>
            </tr>
          </thead>
        )}
        <tbody>
          {rows.map((row) => (
            <tr key={row.dimension}>
              <th scope="row">{row.dimension}</th>
              <td className="cy-compare__without">{row.without}</td>
              <td className="cy-compare__with">
                <i className="cy-compare__mark" aria-hidden="true" />
                {row.with}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {children}
    </section>
  );
}
