import { useId } from 'react';
import type { ReactNode } from 'react';

export interface ComparisonColumn {
  /** Matches a key in every row's `cells`. */
  key: string;
  header: string;
  /** The one column floated out as a card. The pack allows exactly one. */
  us?: boolean;
}

export interface ComparisonRow {
  id: string;
  /** Keyed by column `key`. The first column is the row's label. */
  cells: Record<string, ReactNode>;
}

export interface ComparisonTableProps {
  /** `columns[0]` is the label column; the rest are the things compared. */
  columns: ComparisonColumn[];
  rows: ComparisonRow[];
  /** Says what is being compared. Rendered above the panel and names it. */
  caption?: string;
  className?: string;
}

/**
 * A wide cream panel of 1px-ruled rows with the "us" column lifted out of it as
 * a rounded card in the accent gradient — a physical card laid on a printed
 * table.
 *
 * The panel is a grid rather than a `<table>` because the card is one element
 * spanning every row, which is what makes it read as a single object instead of
 * a column of separately tinted cells. Rows are `display: contents` and every
 * cell is placed explicitly, so the card can sit underneath them all.
 */
export function ComparisonTable({ columns, rows, caption, className }: ComparisonTableProps) {
  const captionId = useId();
  const usIndex = columns.findIndex((column) => column.us === true);

  return (
    <div className={['at-compare', className].filter(Boolean).join(' ')}>
      {caption !== undefined && (
        <p className="at-compare__caption" id={captionId}>
          {caption}
        </p>
      )}
      <div
        className="at-compare__panel"
        role="table"
        aria-labelledby={caption === undefined ? undefined : captionId}
        style={{
          gridTemplateColumns: `minmax(0, 1.6fr) repeat(${Math.max(
            columns.length - 1,
            1,
          )}, minmax(0, 1fr))`,
        }}
      >
        {usIndex >= 0 && (
          <div
            className="at-compare__card"
            aria-hidden="true"
            style={{ gridColumn: `${usIndex + 1}`, gridRow: `1 / ${rows.length + 2}` }}
          />
        )}

        <div className="at-compare__row" role="row">
          {columns.map((column, index) => (
            <div
              key={column.key}
              role="columnheader"
              className={[
                'at-compare__cell',
                'at-compare__cell--head',
                index === 0 ? 'at-compare__cell--label' : undefined,
                column.us === true ? 'at-compare__cell--us' : undefined,
              ]
                .filter(Boolean)
                .join(' ')}
              style={{ gridColumn: `${index + 1}`, gridRow: '1' }}
            >
              {column.header}
            </div>
          ))}
        </div>

        {rows.map((row, rowIndex) => (
          <div key={row.id} className="at-compare__row" role="row">
            {columns.map((column, index) => (
              <div
                key={column.key}
                role={index === 0 ? 'rowheader' : 'cell'}
                className={[
                  'at-compare__cell',
                  index === 0 ? 'at-compare__cell--label' : undefined,
                  column.us === true ? 'at-compare__cell--us' : undefined,
                  rowIndex === rows.length - 1 ? 'at-compare__cell--last' : undefined,
                ]
                  .filter(Boolean)
                  .join(' ')}
                style={{ gridColumn: `${index + 1}`, gridRow: `${rowIndex + 2}` }}
              >
                {row.cells[column.key]}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
