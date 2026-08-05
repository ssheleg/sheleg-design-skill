import type { ReactNode } from 'react';

export interface ComparisonColumn {
  /** Matches a key in every row's `cells`. */
  key: string;
  header: string;
  /**
   * Marks the column the deck is arguing for. Exactly one column carries it;
   * if more than one does, only the first is honoured (see ComparisonTable.md).
   */
  us?: boolean;
}

export interface ComparisonRow {
  id: string;
  cells: Record<string, ReactNode>;
}

export interface ComparisonTableProps {
  /** The first column is normally the criterion being compared. */
  columns: ComparisonColumn[];
  rows: ComparisonRow[];
  /** Mono uppercase line above the table saying what is being compared. */
  caption?: string;
  className?: string;
}

/** The pack's comparison: a table with exactly one column marked as *us*. */
export function ComparisonTable({ columns, rows, caption, className }: ComparisonTableProps) {
  // First flagged column wins, so a second `us` cannot produce a second accent
  // column — the invariant lives here rather than in every caller.
  const usKey = columns.find((column) => column.us === true)?.key;

  return (
    <table className={['br-cmp', className].filter(Boolean).join(' ')}>
      {caption !== undefined && <caption className="br-cmp__caption">{caption}</caption>}
      <thead>
        <tr>
          {columns.map((column) => (
            <th
              key={column.key}
              scope="col"
              className={[
                'br-cmp__th',
                column.key === usKey ? 'br-cmp__th--us' : undefined,
              ]
                .filter(Boolean)
                .join(' ')}
              // The accent is the only visual marker of the us column, so it
              // carries the same claim non-visually.
              aria-current={column.key === usKey ? 'true' : undefined}
            >
              {column.header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => (
          <tr key={row.id} className="br-cmp__row">
            {columns.map((column) => (
              <td
                key={column.key}
                className={[
                  'br-cmp__td',
                  column.key === usKey ? 'br-cmp__td--us' : undefined,
                ]
                  .filter(Boolean)
                  .join(' ')}
              >
                {row.cells[column.key]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
