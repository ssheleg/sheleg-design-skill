import type { ReactNode } from 'react';

export interface DataTableColumn {
  /** Matches a key in every row's `cells`. */
  key: string;
  header: string;
  /** Right-aligns the column and sets it in the data face with tabular figures. */
  numeric?: boolean;
}

export interface DataTableRow {
  id: string;
  cells: Record<string, ReactNode>;
  /**
   * The pack mandates `--accent-weak` plus a 2px accent inset for the selected
   * state, and this component shipped without one until 1.16.0 — the single
   * atom on an admin dashboard that most needs selection was the one that
   * lacked it, while `Chip` implemented the same state correctly.
   */
  selected?: boolean;
}

export interface DataTableProps {
  columns: DataTableColumn[];
  rows: DataTableRow[];
  /** Says what the table is counting. Shown above the header row. */
  caption?: string;
  className?: string;
}

export function DataTable({ columns, rows, caption, className }: DataTableProps) {
  return (
    <div className={['wb-table-wrap', className].filter(Boolean).join(' ')}>
      <table className="wb-table">
        {caption !== undefined && <caption className="wb-table__caption">{caption}</caption>}
        <thead>
          <tr>
            {columns.map((column) => (
              <th
                key={column.key}
                scope="col"
                className={[
                  'wb-table__th',
                  column.numeric === true ? 'wb-table__th--num' : undefined,
                ]
                  .filter(Boolean)
                  .join(' ')}
              >
                {column.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr
              key={row.id}
              className={[
                'wb-table__row',
                row.selected === true ? 'wb-table__row--selected' : undefined,
              ]
                .filter(Boolean)
                .join(' ')}
              aria-selected={row.selected === true ? true : undefined}
            >
              {columns.map((column) => (
                <td
                  key={column.key}
                  className={[
                    'wb-table__td',
                    column.numeric === true ? 'wb-table__td--num' : undefined,
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
    </div>
  );
}
